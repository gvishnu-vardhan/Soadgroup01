import React ,{Component}from 'react';
import axios from 'axios';
import {Redirect} from 'react-router-dom';
class ResetPasswordConfirm extends Component{

state={
    
    reset:false,
    message:'',
}
password={};
confirmpassword={};

  


    handleSubmit=e=>{
        e.preventDefault();
       if(this.password!==this.confirmpassword)
       {
           this.setState({
           message:'Passwords do not match'
           });
       }
       else
       {
        const data={
            password:this.password,
            confirmpassword:this.confirmpassword,
            token:this.props.match.params.token,
            uidb64:this.props.match.params.uidb64,
           
           


        }
    

        
            const config={
                headers:{
                   
                    'Content-Type': 'application/json',
                }
            };
      
     
        console.log(data);
       axios.patch('http://localhost:8000/accounts/password-reset-complete',data,config).then(
             res=>{
                 console.log(res.data);
                 this.setState({
                     reset:true,
                 })
             }
         ).catch(
             err=>{
              
                    this.setState({
                        message:err.response.data.email,
                        
                    })
                
             }
         );

    
            }

    }
    


    render()
    {
        let error='';
        if(this.state.message)
        {
          error=(<div>
            {this.state.message}
          </div>)
        };


        if(this.state.reset){
            return <Redirect to='/login' />
        }
        return(
            <div>
                <h2>Type Password</h2>
              <form onSubmit={this.handleSubmit}>
                  {error}
     <label>
       <br />
       Password:
       <input type="password" name="password" 
       
       onChange={e => this.password=e.target.value}/>
     </label>

     <br />
     <label>
       <br />
      Confirm Password:
       <input type="password" name="password" 
       
       onChange={e => this.confirmpassword=e.target.value}/>
     </label>
      <button type="submit">submit</button>
            </form>
                </div>
        );
    }
}

export default ResetPasswordConfirm;