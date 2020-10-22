import React,{Component}from 'react';
import {Link, Redirect } from 'react-router-dom';
import axios from 'axios';
import Navbar from './Navbar';

class  Login  extends Component {
  state={
    credentials:{email:'',name:'',password:''},
    loggedIn:false,
    message:'',
    
  };
  

login=event=>{
    event.preventDefault();
  console.log(this.state.credentials);
  var data=this.state.credentials
 
  axios.post('http://localhost:8000/accounts/login/',data).then(
      res=>{
        localStorage.setItem('token',res.data.tokens.access);
      
        localStorage.setItem('name',res.data.name);
       this.setState({
         loggedIn:true
       });
       this.props.setUser(res.data);
          
      }).catch(
          err=>{

            this.setState({
              message:err.response.data.detail
            })
          },
          console.log(this.state.message)
      
  )
        };


inputChanged= event=>{
  const cred=this.state.credentials;
  cred[event.target.name]=event.target.value;
  this.setState({credentials:cred});
};





  render()
  {
    if(this.state.loggedIn)
    {
      return <Redirect to={'/'} />;
    }
    
    let error='';
    if(this.state.message)
    {
      error=(<div>
        {this.state.message}
      </div>)
    };



  return (
    <div>
     <h1>Login</h1>
    <p>Login Here</p>
     <form onSubmit={this.login}>
       {error}
     <label>
       <br />
       Email:
       <input type="email" name="email" 
       value={this.state.credentials.email} 
       onChange={this.inputChanged}/>
     </label>
     <br />
     

     <label>
       <br />
       UserName:
       <input type="text" name="name" 
       value={this.state.credentials.name} 
       onChange={this.inputChanged}/>
     </label>
     <br />
     <label>
     
       

       Password:
       <input type="password" name="password"
       value={this.state.credentials.password} 
       onChange={this.inputChanged} />
     </label>
     <button type="submit" >Login</button>
     <Link to={'/password-reset'}>Forgot Password</Link>
     </form>
   

    </div>
  );
}
}

export default Login;
