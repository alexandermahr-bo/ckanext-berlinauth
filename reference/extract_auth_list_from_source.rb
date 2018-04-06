#!/usr/bin/env ruby

require 'csv'
require 'pp'

if (ARGV.length < 2)
    puts "usage: ruby #{__FILE__} AUTH_FOLDER CSV_OUT"
    exit
end

auth_folder_path = ARGV[0]
csv_out_path = ARGV[1]

auth_groups = [ "create", "delete", "get", "patch", "update" ]
auth_method_pattern = /def ([^_].+?)\(context, data_dict.*?\)/

CSV.open(csv_out_path, 'wb') do |csv|
    csv << [ 'group', 'descname', 'anonymous', 'logged_in', 'same_org', 'admin' ]
    Dir.foreach(auth_folder_path) do |file|
        group = File.basename(file, ".py")
        if auth_groups.include?(group)
            puts file
            full_path = File.join(auth_folder_path, file)
            File.open(full_path) do |file_obj|
                auth_functions = file_obj.grep(auth_method_pattern) do |element|
                    element.match(auth_method_pattern)[1]
                end
                pp auth_functions
                auth_functions.each do |function|
                    csv << [ group, function, "-", "-", "-", "+" ]
                end
            end
        end
    end
end