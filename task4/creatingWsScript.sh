read -p "Enter the name of the working space: " name
read -p "Enter the name of the package: " package
mkdir -p $path/$name/src
cd $name
catkin_make
source ~/$name/devel/setup.bash
cd ~/$name/src
catkin_create_pkg $package std_msgs rospy
cd ~/$name
catkin_make
. ~/$name/devel/setup.bash
