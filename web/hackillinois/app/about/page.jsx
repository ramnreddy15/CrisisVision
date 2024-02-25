'use client'
import { useState } from "react";
import Navbar from "../components/navbar";
import { Lexend } from "next/font/google";


const lexend = Lexend({ subsets: ["latin"] })

export default function Page() {
    return (
        <div classname='w=screen h=3000'>
            <Navbar></Navbar>
            <div className="text-black h-[4000px] bg-[#252422]">
                <div className='absolute mb-8 text-6xl text-white top-[150px] w-full flex justify-center'>
                    About the Project
                </div>

                <div className='relative h-[700px] flex flex-row justify-around'>
                    <div className="flex flex-col justify-evenly w-[60%]">
                    <div className='relative text-2xl text-4xl underline text-white top-[250px] flex justify-center w-[40%] left-[25.5%] h-auto text-wrap'>
                        Components
                    </div>
                    <div className="relative text-2xl text-4xl text-white top-[130px] -mt-[40px] flex justify-center w-[60%] left-[25.5%] h-auto">
                        <ul className="list-disc list-inside">
                            <li>Raspberry Pi 4</li>
                            <li>2 Ultrasonic Sensors</li>
                            <li>Arducam 5MP</li>
                            <li>2 DC Motors</li>
                        </ul>
                    </div>
                    </div>
                    <div className="flex flex-col justify-center">
                        <div className='relative rounded-md border-4 border-solid border-white w-[600px] h-[450px] top-[230px] right-[30px] bg-cover bg-no-repeat bg-[url("/bot3.jpg")]'></div>
                    </div>
                </div>

                <div className="relative h-[300px] opacity-50">
                </div>
            <div className='flex flex-row justify-normal'>
                <div className="mt-3 ml-[175px] h-[400px] flex flex-col justify-evenly">
                    <div className='rounded-md border-4 border-solid border-orange-500 relative w-[300px] h-[800px] bg-white bg-cover bg-no-repeat bg-[url("/bot4.jpg")]'> </div>
                </div>
                
                <div className="relative left-[300px]">
                    <div className='relative text-2xl text-4xl underline text-white flex justify-center w-[40%] right-[25.5%] h-auto text-wrap'>
                        Intelligence
                    </div>
                    <div className="relative text-2xl text-4xl text-white top-[60px] -mt-[40px] flex justify-center w-[100%] right-[25.5%] h-auto">
                        <ul className="list-disc list-inside">
                            <li>Auto Obstacle Avoidance</li>
                            <li>Live-feed </li>
                            <li>Object Recognition</li>
                            <li>Panoramic Image Stitching</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div className="relative h-[20px] opacity-50"></div>

            <div className='relative h-[700px] flex flex-row justify-around'>
                    <div className="flex flex-col justify-evenly w-[60%]">
                    <div className='relative text-2xl text-4xl underline text-white flex justify-center w-[40%] left-[25.5%] h-auto text-wrap'>
                        Algorithm
                    </div>
                    <div className="relative text-2xl text-4xl text-white -mt-[200px] flex justify-center w-[60%] left-[25.5%] h-auto">
                        <ul className="list-disc list-inside">
                            <li>Raspberry Pi 4</li>
                            <li>2 Ultrasonic Sensors</li>
                            <li>Arducam 5MP</li>
                            <li>2 DC Motors</li>
                        </ul>
                    </div>
                    </div>
                    <div className="flex flex-col justify-center">
                        <div className='relative rounded-md border-4 border-solid border-white w-[600px] h-[450px] right-[30px] bg-cover bg-no-repeat bg-[url("/bot3.jpg")]'></div>
                    </div>
            </div>

            
            </div>
        </div>
    );
}