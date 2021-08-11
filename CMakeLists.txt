cmake_minimum_required(VERSION 3.0.2)      # CMake的最低版本要求
project(testpkg)

## 以C++ 11標準編譯, 支援 ROS Kinetic 和更新版本
# add_compile_options(-std=c++11)

## 尋找 catkin marcos and libraries
## find_package(catkin REQUIRED COMPONENTS xyz) xyz 改為構建該 package 所需的依賴項
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

## 使用 ROS 以外的功能包時使用的方法
## 例如,使用 Boost 時,必須安裝 system 功能包
# find_package(Boost REQUIRED COMPONENTS system)


## 如果 package 中有 setup.py,則取消此註釋。
## 此 marco 可確保安裝其中宣告的模組和全域腳本
## 參閱 http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
# catkin_python_setup()

################################################
## 宣告 ROS messages, services and actions     ##
################################################

## 如要在這 package 中宣告和建置 messages, services or actions,
## 跟隨以下步驟:
## * 讓 MSG_DEP_SET 是你在 messages/services/actions 中使用其 message 類型
##   的 package 的集合 (e.g. std_msgs, actionlib_msgs, ...).
## * 在檔案 package.xml 中:
##   * 替 "message_generation" 添加一個 build_depend 標籤
##   * 替每個在 MSG_DEP_SET 裡面的 package 添加 build_depend 和 exec_depend 標籤
##   * 如果 MSG_DEP_SET 不是空的,則以下依賴項已被引入
##     但仍可以肯定的宣告：
##     * 替 "message_runtime" 添加一個 exec_depend 標籤
## * 在此檔案 (CMakeLists.txt)中:
##   * 將 "message_generation" 和  MSG_DEP_SET 中的每個 package 添加到
##     find_package(catkin REQUIRED COMPONENTS ...)
##   * 將 "message_runtime" 和  MSG_DEP_SET 中的每個 package 添加到
##     catkin_package(CATKIN_DEPENDS ...)
##   * 根據需要去取消註解下面的 add_*_files 部份 
##     並列出每個要處理的 .msg/.srv/.action 檔案
##   * 取消註解下面的 generate_messages 
##   * 將 MSG_DEP_SET 中的每個 package 添加到 generate_messages(DEPENDENCIES ...)

## 在 'msg' 資料夾中生成 messages
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

## 在 'srv' 資料夾中生成 services
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## 在 'action' 資料夾中生成 actions
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## 使用此處列出的任何依賴項生成添加的 messages 和 services
# generate_messages(
#   DEPENDENCIES
#   std_msgs
# )

################################################
## 宣告 ROS 動態重配置參數                       ##
################################################

## 要在此 package 中宣告和構建動態重配置參數
## 請執行以下步驟:
## * 在 package.xml 中:
##   * 替 "dynamic_reconfigure" 加上 build_depend 和 exec_depend 標籤
## * 在此檔案 (CMakeLists.txt) 中:
##   * 將 "dynamic_reconfigure" 加到
##     find_package(catkin REQUIRED COMPONENTS ...)
##   * 取消註解下面的 "generate_dynamic_reconfigure_options" 
##     並列出要處理的每個 .cfg 檔

## 在 'cfg' 資料夾中生成動態重配置參數
# generate_dynamic_reconfigure_options(
#   cfg/DynReconf1.cfg
#   cfg/DynReconf2.cfg
# )

###################################
## catkin 具體配置                ##
###################################
## The catkin_package macro 替你的 package 生成 cmake config files 
## 宣告要傳遞給依賴項的東西
## INCLUDE_DIRS: 如果你的 package 包含標頭檔的話，取消此註解
## LIBRARIES: 你在這個 project 中創建的 dependent projects 也需要的 libraries
## CATKIN_DEPENDS: dependent projects 也需要的 catkin_packages
## DEPENDS: 這個 project 的 system dependencies 而 dependent projects 也需要的
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES testpkg
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## 指定標頭檔的附加位置
## 你的 package 位置應該在其他位置之前列出
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

## 宣告一個 C++ library
# add_library(${PROJECT_NAME}
#   src/${PROJECT_NAME}/testpkg.cpp
# )

## 加入 the library 的 cmake 目標依賴項 
## 例如, 可能需要在 message generation 
## 或 dynamic reconfigure 的 libraries 之前生成代碼 
# add_dependencies(${PROJECT_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## 宣告一個 C++ 可執行檔
## 使用 catkin_make，所有 packages 都在單個 CMake 上下文中構建
## 推薦的前綴確保跨 package 的目標名稱不會衝突
# add_executable(${PROJECT_NAME}_node src/testpkg_node.cpp)

## 重新命名不帶前綴的 C++ 可執行檔 
## 上面推薦的前綴會導致目標名稱過長，
## 以下將目標重命名回較短的版本以方便用戶使用，
## 例如 "rosrun someones_pkg node" 而不是 "rosrun someones_pkg someones_pkg_node"
# set_target_properties(${PROJECT_NAME}_node PROPERTIES OUTPUT_NAME node PREFIX "")

## 添加與上述庫相同的可執行檔的 cmake 目標依賴項 
# add_dependencies(${PROJECT_NAME}_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## 指定 libraries 以連結 library 或可執行檔
# target_link_libraries(${PROJECT_NAME}_node
#   ${catkin_LIBRARIES}
# )

#############
## Install ##
#############

# 所有安裝目標都應該使用 catkin DESTINATION 變數
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## 標記可執行腳本（Python 等）進行安裝
## 與 setup.py 相比，您可以選擇目的地
# catkin_install_python(PROGRAMS
#   scripts/my_python_script
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## 標記要安裝的可執行文件
## See http://docs.ros.org/melodic/api/catkin/html/howto/format1/building_executables.html
# install(TARGETS ${PROJECT_NAME}_node
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## 標紀要安裝的 libraries 
## See http://docs.ros.org/melodic/api/catkin/html/howto/format1/building_libraries.html
# install(TARGETS ${PROJECT_NAME}
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
# )

## 標紀要安裝的 cpp 標頭檔
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )

## 標記其他文件進行安裝（例如啟動和包文件等）
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############

## 添加基於 gtest 的 cpp 測試目標和鏈接庫
# catkin_add_gtest(${PROJECT_NAME}-test test/test_testpkg.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## 添加要由 python nosetests 測試運行的文件夾
# catkin_add_nosetests(test)
