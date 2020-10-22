import React ,{Component}from 'react';
import {BrowserRouter as Router , Route, Switch} from 'react-router-dom';
import Home from './components/Home';
import Login from './components/Login';
import Register from './components/Register';

import ResetPassword from './components/ResetPassword';
import ResetPasswordConfirm from './components/ResetPasswordConfirm';
import axios from 'axios';
import Navbar from './components/Navbar';
class App  extends Component {
  state={}
  componentDidMount =()=>
  {
      const config={
          headers:{
              Authorization:'Bearer '+localStorage.getItem('token')
          }
      };


      axios.get('http://localhost:8000/accounts/user/'+localStorage.getItem('name')+'/',config).then(
          res=>{
              this.setUser(res.data);
          },
         err=>{
             console.log(err)
         }
      )
  };

  setUser =user =>{
    this.setState({
        user:user
        });
  };


  render()
  {
  return (
  <div>
  
   <Router>
   <Navbar user={this.state.user} setUser={this.setUser}/>
   
     <Switch>
                    <Route exact path='/' component={()=><Home user={this.state.user}/>} />
                    <Route exact path='/login' component={()=><Login setUser={this.setUser}/>} />
                    <Route exact path='/register' component={Register} />
                    <Route exact path='/password-reset/' component={ResetPassword} />
                    <Route exact path='/accounts/password-reset/:uidb64/:token/' component={ResetPasswordConfirm} />
                
       </Switch>
     </Router>
     </div>
  );
}
}

export default App;
