'use client'
import Video from './video'
import Navbar from './navbar'
import { useState } from 'react';

export default function Home() {
  return (
  <div className="w-screen h-[10000px] bg-black">
      <Navbar></Navbar>  
      <div className="w-full h-[900px] bg-cover bg-top bg-no-repeat bg-[url('/bot2.jpeg')] opacity-50">
      </div>
      <div className='absolute text-white top-[200px] left-[100px] text-6xl font-bold w-[85%] h-[50px] flex flex-row justify-center items-center opacity-100'>
        Introducing VentureVision - The next step in disaster relief
      </div>

    <div className="sticky text-white text-5xl mt-10 font-bold top-20 w-full justify-center flex">
      Use Cases
      </div>

    <div className='relative bg-red-100 w-[100%] mt-[100px] h-[700px] flex justify-around'>
        <div className="relative rounded-md w-[75%] h-[560px] bg-cover bg-no-repeat bg-[url('/forestfire.jpg')]">
        </div>
        <div className='absolute bg-green-100 text-white top-40 right-0 w-[25%]'>
          <div className="text-5xl font-bold justify-center mb-6">
            Forest Fires
          </div>
          <div className="text-3xl justify-center text-wrap">
            VentureVision can be used to detect forest fires and alert the proper authorities
          </div>
        </div>
    </div>

    <div className='relative bg-blue-100 w-[100%] mt-[100px] h-[700px] flex flex-col justify-between'>
      <div className="absolute rounded-md w-[825px] h-[560px] right-0 bg-cover bg-no-repeat bg-[url('/hurricaneaftermath.jpg')]">
        <div className='absolute text-white top-400 left-10 w-[300px]'>
          <div className="text-5xl font-bold justify-left mb-6">
            Hurricanes
          </div>
          <div className="text-3xl text-wrap">
            VentureVision can be used to detect hurricane damage and alert the proper authorities
          </div>
        </div>
      </div>
    </div>
    
    





    </div>
  );
}
