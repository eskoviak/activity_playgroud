/**
 * @file connect.cpp
 * @author eskoviak@eskoviak.com
 * @brief 
 * @version 0.1
 * @date 2024-01-20
 * 
 * @copyright Copyright (c) 2024 ESC
 * 
 */

#include "activity.hpp"

pqxx::connection get_pq_connect(){
    try
    {
        std::string uri = std::getenv("PG_LOCAL");
        std::string database = "activity";
        return pqxx::connection{uri+database};
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }
    

};