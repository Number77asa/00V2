import React, { Fragment } from 'react';
import Form from './Form';
import Leads from './Leads';


export default function Dashboard() {
    return (

        <Fragment>
            <Leads />

            <Form />
        </Fragment>

    )
}
//interstingly enough, Leads & Form are the names of the 'rce' components; and the order which we stack them
//is how it shows
