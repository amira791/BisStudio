import React,{useState} from 'react'
import { useParams } from 'react-router-dom';
import { coursesCard } from '../../dummydata';
import { Link } from "react-router-dom"
import PersonIcon from '@mui/icons-material/Person';
import SchoolIcon from '@mui/icons-material/School';
import AddPhotoAlternateIcon from '@mui/icons-material/AddPhotoAlternate';

const Payment = () => {

  const [formData, setFormData] = useState({
    name: '',
    familyName: '',
    photo: null, // This will hold the selected photo
  });

  const { id } = useParams();
    // Find the course details based on the ID
  const course = coursesCard.find((course) => course.id === parseInt(id));
  const handleChange = (e) => {
    const { name, value, type, files } = e.target;

    // If the input is a file input, set the selected file in the state
    if (type === 'file') {
      setFormData({ ...formData, [name]: files[0] });
    } else {
      setFormData({ ...formData, [name]: value });
    }
  };

  return (
    <div  className='containerl' >
       <div className='headerl'>
            <div className='textl'> Payment </div>
            <div className='underlinel'> </div>
            
        </div>
      <div>
      {course ? (
        <div >
          <h1>{course.coursesName}</h1>
        
        </div>
      ) : (
        <p>Course not found</p>
      )}
    </div>
    <div className='inputsl'>
    <div className='inputl'>
    <div className='imgl'>
      < PersonIcon/>
        </div>
      <input type='textl' placeholder=' Enter your Name '/>
      </div>
     
      <div className='inputl'>
        <div className='imgl'>
          < PersonIcon/>
        </div>
      <input type='textl' placeholder=' Enter your Name '/>
      </div>
      <div className='inputl'>
        <div className='imgl'>
          < PersonIcon/>
        </div>
      <input type='textl' placeholder=' Enter your Family Name '/>
      </div>
     
      <div className='inputl'>
        <div className='imgl'>
        <SchoolIcon />
        </div>
      <input type='textl' placeholder=' Enter your study branche  '/>
      </div>
      <div  className='inputl' >
           <div className='imgl'>
            <AddPhotoAlternateIcon/>
            </div> 
            add payment
        <input
          placeholder='Drop A payment photo'
          type="file"
          name="photo"
          accept="image/*" // Accept only image files
          onChange={handleChange}
        />
      </div>
      <button>
        Submit
      </button>
      

      </div>
      </div>
 
    
   
  )
}

export default Payment