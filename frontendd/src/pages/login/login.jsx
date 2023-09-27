import React,{useState} from 'react'
import './login.css'
import PersonIcon from '@mui/icons-material/Person';
import EmailIcon from '@mui/icons-material/Email';
import LockIcon from '@mui/icons-material/Lock';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import SchoolIcon from '@mui/icons-material/School';
import AccountBoxIcon from '@mui/icons-material/AccountBox';

const Login  = () => {
  const [action, setAction ]=useState("Login")
  const [email, setEmail] = useState('');

  const [password, setPassword] = useState('');
  
  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleLogin = () => {
    // You can add your login logic here, such as making an API request to authenticate the user.
    // For this example, we'll just display the entered email and password in an alert.
    console.log("Logging in with email:", email, "and password:", password)
    
    alert(`Email: ${email}\nPassword: ${password}`);
  };


  return (
    <div className='all'>
    <div className='containerl'>
        <div className='headerl'>
            <div className='textl'>{action}
             </div>
            <div className='underlinel'> </div>
            
        </div>
        <div className='inputsl'>
          {action==="Login"?<div></div>:  <div className='inputl'>
              <div className='imgl'>
            < PersonIcon/>
            </div>
            <input type='textl' placeholder=' Enter your Name '/>
            </div> }
            {action==="Login"?<div></div>:  <div className='inputl'>
              <div className='imgl'>
            < PersonIcon/>
            </div>
            <input type='textl' placeholder=' Family Name  '/>
            </div> }
            {action==="Login"?<div></div>:  <div className='inputl'>
              <div className='imgl'>
            < AccountBoxIcon/>
            </div>
            <input type='textl' placeholder=' User Name '/>
            </div> }
            {action==="Login"?<div></div>:  <div className='inputl'>
              <div className='imgl'>
            < LocationOnIcon/>
            </div>
            <input type='textl' placeholder=' Wilaya '/>
            </div> }
            {action==="Login"?<div></div>:  <div className='inputl'>
              <div className='imgl'>
            <SchoolIcon />
            </div>
            <input type='textl' placeholder='Year & Branche : 1as science '/>
            </div> }
            <div className='inputl'>
            <div className='imgl'>
            <EmailIcon/>
            </div>

            <input type='emaill'
             id="email"
             placeholder=' Email'
             value={email}
             onChange={handleEmailChange}
            />
            </div>
            <div className='inputl '>
            <div className='imgl'>
            <LockIcon/>
            </div>
            <input type='passwordl '
             placeholder='Password '
             value={password}
             id="password"
             onChange={handlePasswordChange}/>
            </div>
        </div>
        {action==="Sign Up"?<div></div>:  <div className='forgot-passwordl'> Lost password ?<span>Click here!</span></div>}
      
        <div className='submit-containerl'>
            <div className={action==="Login"?"submitl gray":"submitl"} onClick={()=>{setAction("Sign Up")}}>Sign Up</div>
            <div className={action ==="Sign Up"? "submitl gray":"submitl"} onClick={handleLogin}>Login </div>

        </div>
        

    </div>
    </div>
  
  )
}
export default Login