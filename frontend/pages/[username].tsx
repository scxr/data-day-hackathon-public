import React from 'react';

import Head from 'next/head';

import { useRouter } from 'next/router';
import { isWebUri } from 'valid-url';

import { NextPageContext } from 'next';

export default function UserPage({ accounts }) {
  const router = useRouter();
  const { username } = router.query;

  console.log(accounts);

  return (
    <div className='flex flex-col items-center'>
      <Head>
        <title>{ username } - Where Am I Online?</title>
      </Head>
      <div className='flex justify-center bg-yellow-500 w-full mb-8'>
        <h1 className='font-bold font-mono text-5xl'>{ username }</h1>
      </div>
      { Object.keys(accounts).map((service, idx) => {
        const account = accounts[service];

        if (typeof account == 'string' || account == null) return null;

        return (
          <a key={ idx } href={ account.url } className='block no-underline w-11/12 md:w-2/5'>
            <div className='flex flex-col p-2'>
              <h3 className='text-2xl m-0 mb-1'>{ service }</h3>
              <div className='flex flex-row items-center'>
                <img className='rounded-full mr-2' src={ account.pfp_url || 'https://www.clipartkey.com/mpngs/m/29-297748_round-profile-image-placeholder.png' } width={ 50 }/>
                <h3 className='text-xl m-0'>{ account.name }</h3>
              </div>
              <div className='flex flex-row flex-wrap'>
                {
                  Object.entries(account)
                    .filter(entry => !['pfp_url', 'name', 'url'].includes(entry[0]) && entry[1])
                    .map(([field, value], idx) => {
                      let valueShown = value;

                      if (typeof value == 'boolean') {
                        valueShown = (
                          <span className={ value ? 'text-green-500' : 'text-red-500' }>
                            { value ? '✓' : '✗' }
                          </span>
                        );
                      } else if (typeof value == 'number' && value > 1000000000) {
                        valueShown = new Date(value * 1000).toLocaleDateString();
                      } else if (typeof value =='string' && isWebUri(value)) {
                        valueShown = (
                          <a href={ value as string }>
                            { new URL(value as string).origin }
                          </a>
                        );
                      } else if (typeof value == 'number') {
                        valueShown = value.toLocaleString();
                      }

                      return (
                        <div key={ idx } className='flex flex-col p-3'>
                          <span className='font-bold text-lg'>{ field.replace('_', ' ') }</span>
                          <span className='font-normal'>
                            { valueShown }
                          </span>
                        </div>
                      );
                    })
                }
              </div>
            </div>
          </a>
        );
      }) }
    </div>
  );
}

export async function getServerSideProps(context: NextPageContext) {
  const { query: { username } } = context;
  const API_URL = 'https://data-day-hackathon.herokuapp.com/';

  const accounts = await fetch(API_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ username })
  })
    .then(res => res.json());

  return {
    props: {
      accounts 
    }
  };
}
