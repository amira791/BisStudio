import React from 'react'
import { useParams } from 'react-router-dom';
import { coursesCard } from '../../dummydata';
import { Link } from "react-router-dom"
import SchoolIcon from '@mui/icons-material/School';

const Course = () => {
  const { id } = useParams();

  // Find the course details based on the ID
  const course = coursesCard.find((course) => course.id === parseInt(id));

  return (
    <div>
    <div>
      {course ? (
        <div>
           <div className='dimg'>
            <img src={course.cover} alt='' />
            </div>
          <h1>{course.coursesName}</h1>
       
          {course.priceAll}
          {course.pricePer}
          description
          
        </div>
      ) : (
        <p>Course not found</p>
      )}
    </div>
    <Link to='/Payment/:id'>
    <button> Buy Now </button>
    </Link>
    </div>
  );
}

export default Course