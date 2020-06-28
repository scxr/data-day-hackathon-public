import React, { useState } from 'react';

import Head from 'next/head';
import Particles from 'react-particles-js';

import { useRouter } from 'next/router';

export default function Home() {
  const [username, setUsername] = useState('');

  const router = useRouter();

  const onSubmit = (e: any) => {
    e.preventDefault();
    router.push(`/${ username }`);
    return false;
  };

  return (
    <div>
      <Head>
        <title>Where Am I Online?</title>
      </Head>
      <Particles
        className='w-screen h-screen'
        params={{
	        'particles': {
	          'number': {
	            'value': 25
	          },
	          'size': {
	            'value': 3
            },
            'color': {
              'value': '#0d47a1'
            },
            'links': {
              'color': {
                'value': '#0d47a1'
              }
            }
          },
	        'interactivity': {
	          'events': {
	            'onhover': {
	              'enable': true,
	              'mode': 'repulse'
	            }
	          }
	        }
	    }}/>
      <div className='font-sans w-full' style={ { position: 'absolute', top: 0, left: 0 } }>
        <div className='flex flex-col items-center justify-center pt-16 pb-16'>
          <div className='flex flex-row mb-2'>
            <img src='/zondicons/search.svg' className='animation-sweeping' width={ 40 }/>
            <h1 className='font-bold text-5xl ml-2'>Where Am I Online?</h1>
          </div>
          <form className='flex flex-row w-11/12 md:w-1/2' onSubmit={ onSubmit }>
            <input
              className='block text-lg w-full p-3'
              placeholder='Username'
              value={ username }
              onChange={ e => setUsername(e.target.value) }
            />
            <button className='block text-lg' type='submit'>
              Go
            </button>
          </form>
        </div>
        <div className='flex flex-col md:flex-row items-center justify-center bg-yellow-500 font-bold text-xl text-center w-full py-4 md:py-12'>
          <div className='flex items-center justify-center block fixed card'>
            <p>
              Input a username
            </p>
          </div>
          <hr className='line md:border-b-4'/>
          <div className='flex items-center justify-center block fixed card'>
            <p>
              We search for matching social media accounts
            </p>
          </div>
          <hr className='line md:border-b-4'/>
          <div className='flex items-center justify-center block fixed card'>
            <p>
              Explore a user's online presence
            </p>
          </div>
        </div>
        <div className='block fixed font-bold text-center w-11/12 md:w-2/5 mx-auto my-8'>Created for Data Day Grind 2020</div>
      </div>
    </div>
  );
}
