/**
 * @file activity.cpp
 * @author eskoviak@eskoviak.com    
 * @brief main library file
 * @version 0.1
 * @date 2024-01-20
 * 
 * @copyright Copyright (c) 2024 ESC
 * 
 */

#include "activity.hpp"

std::map<int, std::string> get_exercises()
{
    pqxx::connection c = get_pq_connect();
    pqxx::work txn{c};

    std::map<int, std::string> exercises;
    pqxx::result r = txn.exec("SELECT id, exercise_name FROM public.exercises");
      
    for(const auto &row : r) {    
      int id = row[0].get<int>().value_or(0);
      std::string exercise_name = row[1].c_str();
      const auto [it, success] = exercises.insert({id, exercise_name});
    }

    return exercises;
}