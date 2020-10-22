import React,{Component}from 'react';
import {Redirect} from 'react-router-dom';
import axios from 'axios';


class  Register  extends Component {
  state={
    credentials:{email:'',name:'',aadharnumber:'',person:'',password:''},
    message:'',
    registered:false,
  }
  

register=event=>{
  let message1='';
    event.preventDefault();
  console.log(this.state.credentials);
  
  var data=this.state.credentials;
  axios.post('http://localhost:8000/accounts/register/',data).then(
      res=>{
          console.log(res)
          this.setState({
            registered:true
          })
         


      }).catch(
          err=>{

            if(err.response && err.response.data.email)
            {
              message1=err.response.data.email
            }
            else if(err.response && err.response.data.name)
            {
              message1=err.response.data.name
            }
            else if(err.response && err.response.data.aadharnumber)
            {
              message1=err.response.data.aadharnumber
            }
            else if(err.response && err.response.data.person)
            {
              message1=err.response.data.person
            }
           
            else if(err.response && err.response.data.error)
            {
              message1=err.response.data.error
            }
            else
            {
              if(err.response)
              {
              message1=err.response.data.password
              }
            }
              this.setState(
                {
                
                 message:message1
                 
                }
              )

          },
          console.log(this.state.message)
      
  )
        }


inputChanged= event=>{
  const cred=this.state.credentials;
  cred[event.target.name]=event.target.value;
  this.setState({credentials:cred});
}

  render()
  {
    if(this.state.registered)
    {
      

      return <Redirect to={'/login'} />
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
     <h1>Sign Up</h1>
     <p>Create your Account</p>
     <form onSubmit={this.register}>
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
     AadharNumber:
       <input type="text" name="aadharnumber" 
       value={this.state.credentials.aadharnumber} 
       onChange={this.inputChanged}/>
     </label>
     <br />
    

     <label>person
        <select  value={this.state.credentials.person} id="person" name='person'  type='text'  onChange={this.inputChanged}>
          <option value="-1">Choose your Title</option>
            <option value="0">Customer</option>
            <option value="1">Owner</option>
         
          </select>
          
          </label>
          <br />
<label>
       Password:
       <input type="password" name="password"
       value={this.state.credentials.password} 
       onChange={this.inputChanged} />
     </label>
      <br />
   

     <button type="submit" >Register</button>
     </form>
    </div>
  );
}
}

export default Register;
