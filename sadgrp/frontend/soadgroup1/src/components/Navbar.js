import React ,{Component}from 'react';
import {Link} from 'react-router-dom';
class Navbar extends Component{
    
    handleLogout=()=>{
        localStorage.clear();
        this.props.setUser(null);
    }

    render(){
        let  buttons;
        if(this.props.user)
        {
            buttons=(
            <div>
            
            <Link to={"/"} onClick={this.handleLogout}>Logout</Link>
            </div>
            )
        }
        else{
     buttons=(
         <div>
                <Link to={"/register"}>Register</Link>
                <Link to={"/login"}>Login</Link>
                </div>
     )
        }


        return(
            <div>
                <nav>
                <Link to={"/"}>Home</Link>
                
                {buttons}
                
                </nav>
                </div>
        );
    }
}

export default Navbar;