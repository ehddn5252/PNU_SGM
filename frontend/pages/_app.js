import React from 'react';
import Head from 'next/head';

// style
import '../styles/utils.scss';
import '../styles/dashboard.scss';
import '../styles/index.scss';

// components style
import '../styles_components/filter.scss'
import '../styles_components/subgraph.scss'
import '../styles_components/maingraph.scss'

const Songgolmae = ({Component}) => {
    return (
        <>
            <Head>
                <title>???</title>
            </Head>
            <Component/>
        </>
    );
};

export default Songgolmae;