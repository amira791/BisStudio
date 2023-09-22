import "./App.css"
import Header from "./components/common/header/Header"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"
import About from "./components/about/About"
import CourseHome from "./components/allcourses/CourseHome"
import Team from "./components/team/Team"
import Pricing from "./components/pricing/Pricing"
import Blog from "./components/blog/Blog"
import Contact from "./components/contact/Contact"
import Footer from "./components/common/footer/Footer"
import Home from "./components/home/Home"
import login from "./pages/login/login"
function App() {
  return (
    <>
      <Router>
      <Switch>
        {/* Routes without header and footer */}
        <Route exact path='/Login' component={login} />
        
        {/* Routes with header and footer */}
        <Route path={['/', '/about', '/courses', '/team', '/pricing', '/journal', '/contact']} >
          <Header />
          <Route exact path='/' component={Home} />
          <Route exact path='/about' component={About} />
          <Route exact path='/courses' component={CourseHome} />
          <Route exact path='/team' component={Team} />
          <Route exact path='/pricing' component={Pricing} />
          <Route exact path='/journal' component={Blog} />
          <Route exact path='/contact' component={Contact} />
          <Footer />
        </Route>
      </Switch>
    </Router>
    </>
  )
}

export default App
