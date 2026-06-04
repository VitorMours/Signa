import "package:flutter/material.dart";

class BottomNavBar {
  @override
  Widget build(BuildContext context){
    return BottomNavigationBar(items: [
      BottomNavigationBarItem(icon: Icon(Icons.home), label:'home'),
      BottomNavigationBarItem(icon: Icon(Icons.camera_alt), label:'camera'),
      BottomNavigationBarItem(icon: Icon(Icons.book), label:'notes'),
      BottomNavigationBarItem(icon: Icon(Icons.person), label:'profile'),
    ]);
  }

}
