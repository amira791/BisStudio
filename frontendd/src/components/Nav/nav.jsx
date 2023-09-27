import React,{useState} from 'react'
import { coursesCard } from '../../dummydata';
import { Link } from "react-router-dom"
import './nav.css'

const Nav  = () => {
    const [searchTerm, setSearchTerm] = useState("");
  return (
    <>
    <div>
      <div className="searchInput_Container">
        <input id="searchInput" type="text" placeholder="Search here..." onChange={(event) => {
          setSearchTerm(event.target.value);
        }} />
      </div>
      <div className="container grid2">
        {
          coursesCard 
            .filter((val) => {
              if(searchTerm == ""){
                return val;
              }else if(val.coursesName.toLowerCase().includes(searchTerm.toLowerCase())){
                return val;
              }
            })
            .map((val) => {
              return(
                <div className="coursesCard" >
                 <div className='items' >
            <Link to={`course/${val.id}`} className='course-link'>
              <div className='content flex'>
                <div className='left'>
                  <div className='img'>
                    <img src={val.cover} alt='' />
                  </div>
                </div>
                <div className='text'>
                  <h1>{val.coursesName}</h1>
                  <div className='rate'>
                    <i className='fa fa-star'></i>
                    <i className='fa fa-star'></i>
                    <i className='fa fa-star'></i>
                    <i className='fa fa-star'></i>
                    <i className='fa fa-star'></i>
                    <label htmlFor=''>(5.0)</label>
                  </div>
                  <div className='details'>
                    {val.courTeacher.map((details) => (
                      <>
                        <div className='box'>
                          <div className='dimg'>
                            <img src={details.dcover} alt='' />
                          </div>
                          <div className='para'>
                            <h4>{details.name}</h4>
                          </div>
                        </div>
                        <span>{details.totalTime}</span>
                      </>
                    ))}
                  </div>
                </div>
              </div>
              <div className='price'>
                <h3>
                  {val.priceAll} / {val.pricePer}
                </h3>
              </div>
              <button className='outline-btn'>ENROLL NOW !</button>
              </Link>
            </div>
                </div> 
              )
            })
        }
      </div>
    </div>
  </>
  )
}

export default Nav