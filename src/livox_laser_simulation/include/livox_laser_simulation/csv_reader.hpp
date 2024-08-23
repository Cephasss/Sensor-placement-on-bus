//
// Created by lfc on 2021/3/1.
//

#ifndef SRC_GAZEBO_CSV_READER_HPP
#define SRC_GAZEBO_CSV_READER_HPP

#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <unistd.h>
#include <pwd.h>

class CsvReader {
 public:
    static bool ReadCsvFile(std::string file_name, std::vector<std::vector<double>>& datas) {
        file_name = ExpandTilde(file_name);
        std::fstream file_stream;
        file_stream.open(file_name, std::ios::in);
        if (file_stream.is_open()) {
            std::string header;
            std::getline(file_stream, header, '\n');
            while (!file_stream.eof()) {
                std::string line_str;
                std::getline(file_stream, line_str, '\n');
                std::stringstream line_stream;
                line_stream << line_str;
                std::vector<double> data;
                try {
                    while (!line_stream.eof()) {
                        std::string value;
                        std::getline(line_stream, value, ',');
                        data.push_back(std::stod(value));
                    }
                } catch (...) {
                    std::cerr << "cannot convert str:" << line_str << "\n";
                    continue;
                }
                datas.push_back(data);
            }
            std::cerr << "data size:" << datas.size() << "\n";
            return true;
        } else {
            std::cerr << "cannot read csv file!" << file_name << "\n";
        }
        return false;
    }
    
    private:
    static std::string ExpandTilde(const std::string& path) {
        if (!path.empty() && path[0] == '~') {
            if (path.size() == 1 || path[1] == '/') {
                const char* home = getenv("HOME");
                if (home || (home = getpwuid(getuid())->pw_dir)) {
                    return std::string(home) + path.substr(1);
                }
            }
        }
        return path;
    }
};

#endif  // SRC_GAZEBO_CSV_READER_HPP
