import React ,{Component}from 'react';
import axios from 'axios';
class ResetPassword extends Component{

state={
    credentials:{email:''},
    message:'',
}

  


    handleSubmit=e=>{
        e.preventDefault();
        var data=this.state.credentials;
         axios.post('http://localhost:8000/accounts/request-reset-email/',data).then(
             res=>{
                this.setState({
                    message:res.data.success,
                    cls:'success'
                })
             }
         ).catch(
             err=>{
                 this.setState({
                     message:err.response.data.email,
                     cls:'danger'
                 })
             }
         )

    };



    inputChanged= event=>{
        const cred=this.state.credentials;
        cred[event.target.name]=event.target.value;
        this.setState({credentials:cred});
      }
      


    render(){
        let error='';
        if(this.state.message)
        {
          error=(<div>
            {this.state.message}
          </div>)
        };

        return(
            <div>
                <h2>Forgot Password</h2>
              <form onSubmit={this.handleSubmit}>
                  {error}
     <label>
       <br />
       Email:
       <input type="email" name="email" 
       value={this.state.credentials.email} 
       onChange={this.inputChanged}/>
     </label>
     <br />
      <button type="submit">submit</button>
            </form>
                </div>
        );
    }
}

export default ResetPassword;