import React, {useReducer, useState } from 'react';
import axios from "axios";



const Register = (props) => {

    const [formData, setFormData] = useState({
        email: '',
        name: '',
        password: '',
        re_password: '',
    });

    const [formError, setFormError] = useState('')

    // This is called destructuring. It cleans up the code by simplifying the variables. 
    // A short example is user.email = email after destructuring
    const {email, name, password, re_password} = formData;


    const onChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value});
    }


    const onSubmit = e => {
        e.preventDefault();
        if(password == re_password){
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };
        const body = JSON.stringify({email, name, password, re_password});
        axios.post(`${process.env.REACT_APP_API_URL}/auth/users/`, body, config)
        .then(function(res){
            // Clear the register form data if successful
            setFormData({...formData, [name]: ''});
            setFormData({...formData, [email]: ''});
            setFormData({...formData, [password]: ''});
            setFormData({...formData, [re_password]: ''});
            // Set the auth box to the login componenet
            props.setComponent('login')


            // set a global variable with the login status and the login response
            // Look at 24:56 on the video mentions in notes
        }).catch(function(res){
            console.log(res.response.data)
            if (res.response.data['email'] != undefined) {
                setFormError(res.response.data['email'])
            } else {
                setFormError(res.response.data['password'])
            }
        });
    } else {
        setFormError('Passwords do not match!')
    }
        
    };

    //is user authenticated?
    //redirectr to home page
    return ( 
        <form className="auth-form" onSubmit={e => onSubmit(e)} >
            <div className="auth-input">
            {/* Name input field  */}
            <input 
            className='form-input' 
            type="text" 
            placeholder='Name' 
            name="name" 
            value={name}
            onChange={e => onChange(e)}
            required
            />
            {/* Email input field  */}
            <input 
            className='form-input' 
            type="email" 
            placeholder='Email' 
            name="email" 
            value={email}
            onChange={e => onChange(e)}
            required
            />
            {/* Password input field */}
            <input 
            className='form-input'  
            type="password" 
            placeholder='Password'
            name="password"
            value={password}
            onChange={e => onChange(e)}
            minLength='6'
            required
            />
            {/* Confirm Password input field */}
            <input 
            className='form-input'  
            type="password" 
            placeholder='Retype Password'
            name="re_password"
            value={re_password}
            onChange={e => onChange(e)}
            minLength='6'
            required
            />
            </div>
            <div className='error-msg'>
            <p>{formError}</p>
            </div>
            
            {/* Action buttons */}
            <div
             className='form-btns'>
                 <button className='btn' type="submit">Register</button>
            </div>
            
        </form>
    
     );
}

// const mapStateToProps = state = => ({
//     //is authenticated?
// })

export default Register;