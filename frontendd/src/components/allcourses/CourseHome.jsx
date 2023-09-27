import React from "react"
import Back from "../common/back/Back"
import CoursesCard from "./CoursesCard"
import OnlineCourses from "./OnlineCourses"
import { Link } from "react-router-dom"
import Nav from "../Nav/nav"
import Course from "../../pages/course/course"


const CourseHome = () => {
  return (
    <>
      <Back title='Explore Courses' />
      <Nav />
      <Course/>
     
    </>
  )
}

export default CourseHome
