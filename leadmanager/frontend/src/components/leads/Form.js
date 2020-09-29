//this is the actual template on dashboard where we enter info. 
//note last line in this is: connect(null) --> because were noy carrying any info over
//unlike ./leads.js last line is connect (get leads ); thats b/c those are carried fro  this one

import React, { Component } from 'react'
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addLead } from '../../actions/leads';
import './Form.css';
import si from "./search-icon.png";
import poke from "./poke.jpg";
import Juices from "./Juices.jpg";
import Ceviche from "./cici23.jpg";
import Sush from "./sush.jpg";
import { Link } from "react-router-dom";


export class Form extends Component {
    //ets add a state, beause in react 
    //when you have a form you want each input to be part of the state in hte componenet
    state = {
        name: '',

        message: ''
    }

    //on change takes in event and inside setState we put in our state object
    onChange = e => this.setState({
        [e.target.name]:
            e.target.value
    });

    static propTypes = {
        addLead: PropTypes.func.isRequired
    }

    onSubmit = e => {
        e.preventDefault();
        const { name, message } = this.state;
        const lead = { name, message };
        this.props.addLead(lead);
        this.setState({
            name: "",

            message: ""
        });
    };


    //below we have a form has a event on submit, it will call this.onsubmit
    //we have each input that has an on change (up above)
    //when we type anything in the form, it will fire on change off and need to update state b/ each input is connectd piece of state


    render() {

        const guestLinks = (
            <ul className="navbar-nav ml-auto mt-2 mt-lg-0">
                <li className="nav-item">

                    <Link to="/login" className="nav-link">
                        Login
             </Link>
                </li>
            </ul>
        );
        //const below pulls out the value names from way below
        const { name, message } = this.state;
        return (
            <div className="card-group12">
                <div className="container-fluid">

                    <div className="col-sm-6 m-auto">
                        <div className="card card-body mt-5">

                            <h2>Call 7739909745 to Order or {guestLinks} </h2>

                            <form onSubmit={this.onSubmit}>
                                <div className="form-group">
                                    <label>Name, Address (Apt# or Suite#), Phone </label>
                                    <input
                                        className="form-control"
                                        type="text"
                                        name="name"
                                        onChange={this.onChange}
                                        value={name}
                                    />
                                </div>

                                <div className="form-group">
                                    <label>Please submit your order here</label>
                                    <textarea
                                        className="form-control"
                                        type="text"
                                        name="message"
                                        onChange={this.onChange}
                                        value={message}
                                    />
                                </div>
                                <div className="form-group">
                                    <button type="submit" className="btn btn-primary">
                                        Submit
                             </button>
                                </div>
                            </form>
                        </div>
                    </div>
                    <div className="demo">
                        <div className="grid">



                            <div className="wrapper padded-container">
                                <div className="card-image">
                                    <center><img src={Ceviche} /></center>
                                </div>
                            </div>


                            <div className="wrapper padded-container">
                                <div id="one">
                                    <div className="card-image">

                                        <center><img src={poke} /></center>
                                    </div>
                                </div>
                            </div>


                            <div className="wrapper padded-container">
                                <div className="card-image">
                                    <center><img src={Juices} /></center>
                                </div>
                            </div>

                        </div>
                    </div>


                </div>
            </div>

        )



    }

}


export default connect(null, { addLead })(Form);
