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
auth_method_pattern = /is_authorized(_boolean)?\([^']*?'([^']+?)'/m

CSV.open(csv_out_path, 'wb') do |csv|
    csv << [ 'group', 'descname', 'anonymous', 'logged_in', 'same_org', 'admin' ]
    auth_functions = []
    Dir.foreach(auth_folder_path) do |file|
        group = File.basename(file, ".py")
        if auth_groups.include?(group)
            puts file
            full_path = File.join(auth_folder_path, file)
            code = File.read(full_path)
            result = code.scan(auth_method_pattern)
            result = result.map { |match| match[1] }.uniq
            auth_functions = auth_functions + result
        end
    end
    auth_functions.uniq!.sort!
    pp auth_functions
    auth_functions.each do |function|
        csv << [ function, "-", "-", "-", "+" ]
    end
end