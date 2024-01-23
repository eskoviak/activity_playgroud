/**
 * @file libtest.cpp
 * @author eskoviak@eskoviak.com   
 * @brief Test file for libactivity
 * @version 0.1
 * @date 2024-01-21
 * 
 * @copyright Copyright (c) 2024 ESC
 * 
 */

#include "../activity.hpp"

int main() 
{
    std::map<int, std::string> exercises = get_exercises();

    for (const auto& [id, name] : exercises)
    {
      std::cout << id << '-' << name << std::endl;
    }
}
