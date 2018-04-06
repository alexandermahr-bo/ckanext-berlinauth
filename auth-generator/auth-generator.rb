#!/usr/bin/env ruby

require 'csv'

class AuthGenerator
    def initialize(conf)
        @indent = conf[:indent]
    end

    def _generate_code(code_array)
        indent = " " * @indent
        code = code_array.map{ |line| line.gsub("\t", indent) }.join("\n")
        return code
    end

    def generate_boilerplate
        code = [
            "\# encoding: utf-8" ,
            "" ,
            "\# This is auto-generated code!" ,
            "" ,
            "import logging" ,
            "import ckan.plugins as plugins" ,
            "import ckan.model as model" ,
            "from ckan.common import c" ,
            "" ,
            "log = logging.getLogger(__name__)" ,
            "" ,
            "" ,
        ]
        return _generate_code(code)
    end

    def generate_plugin_class(class_name, method_names)
        code = [
            "class #{class_name}(plugins.SingletonPlugin):" ,
            "\tplugins.implements(plugins.IAuthFunctions)" ,
            "\t" ,
            "\tdef get_auth_functions(self):" ,
            "\t\treturn {" ,
        ]

        method_names.each do |method_name|
            code << "\t\t\t'#{method_name}': #{method_name} ,"
        end

        code << "\t\t}"
        return _generate_code(code)
    end
    
    def generate_auth_method_snippet(method_name, permissions)
        code = [
            "def #{method_name}(context, data_dict=None):"
        ]

        if permissions[:anonymous]
            code.insert(0, "@plugins.toolkit.auth_allow_anonymous_access")
            code << "\treturn { 'success': True }"
        elsif permissions[:admin]
            code << "\treturn { 'success': c.userobj.sysadmin }"
        else
            code << "\treturn { 'success': False }"
        end

        return _generate_code(code)
    end

end

if (ARGV.length < 3)
    puts "usage: ruby #{__FILE__} CSV_IN PYTHON_OUT CLASS_NAME"
    exit
end

csv_in_path = ARGV[0]
python_out_path = ARGV[1]
plugin_class_name = ARGV[2]

generator_config = {
    :indent => 2
}
generator = AuthGenerator.new(generator_config)

CSV::Converters[:plus_minus_boolean] = lambda do |value|
    if value == "+"
        return true
    elsif value == "-"
        return false
    else
        return value
    end
end

puts  "generating #{python_out_path} from #{csv_in_path} ..."

File.open(python_out_path, "w") do |out|

    out.puts(generator.generate_boilerplate)
    out.puts
    method_names = []

    CSV.foreach(csv_in_path, :headers => true, :converters => [:plus_minus_boolean], :header_converters => :symbol) do |row|
        method_name = row[:descname]
        method_names << method_name
        permissions = row.to_hash.select {|key, value| [:anonymous, :logged_in, :same_org, :admin].include?(key) }
        out.puts(generator.generate_auth_method_snippet(method_name, permissions))
        out.puts
    end

    out.puts(generator.generate_plugin_class(plugin_class_name, method_names))
    out.puts
end

puts "... done."