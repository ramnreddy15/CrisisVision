'use client'
import { useState } from "react";
import Navbar from "../components/navbar";

export default function Page(){
    const [asdf, setAsdf] = useState('')
    if (typeof window !== "undefined") {
        window.addEventListener('scroll', () => {
            const scrolled = window.scrollY
            console.log(window.scrollY)

            if (scrolled >= 50) {
                setAsdf('black')
            } else {
                setAsdf('')
            }

        })
    }
    return(
        <div classname='w=screen h=3000'>
            <Navbar></Navbar>
            <div className="text-black h-[1200px] bg-[#252422]">
                <div className='absolute mb-8 text-6xl text-white top-[150px] w-full flex justify-center'>
                    The Team
                </div>

                <div className='relative h-[35%] flex flex-row justify-around'>
                    <div className='relative text-2xl text-white top-[320px] flex justify-center w-[30%] left-[7.5%] h-auto text-wrap'>
                        We are a team of 4 students from the University of Illinois at Urbana-Champaign and the University of California, Irvine. We are all passionate about technology and its potential to solve real-world problems. 
                        We are excited to be a part of HackIllinois and to have the opportunity to work on a project that has the potential to make a real impact.
                    </div>
                    <div className="flex flex-col justify-center">
                        <div className='relative rounded-md border-4 border-solid border-white w-[600px] h-[450px] top-[300px] right-[30px] bg-cover bg-no-repeat bg-[url("/team.jpg")]'></div>
                    </div>
                </div>

                <div className="relative h-[30%] opacity-50">
                </div>
            <div className='flex flex-row justify-normal'>
                <div className="mt-3 ml-[175px] h-[400px] flex flex-col justify-evenly">
                    <div className='rounded-md border-4 border-solid border-orange-500 relative w-[400px] h-[145px] bg-white bg-cover bg-no-repeat bg-[url("/grainger.png")]'> </div>
                    <div className='rounded-md border-4 border-solid border-blue-500 relative w-[400px] h-[200px] bg-cover bg-no-repeat bg-[url("/ucieng_logo.png")]'> </div>
                </div>
                
                <div className="relative left-[300px]">
                <div className='mt-10 relative w-[100px] h-[25px] left-[15px] bg-cover bg-no-repeat bg-[url("/linkedin1.png")]'> </div>
                    <ul className="text-white mt-10">
                        <li className="m-4"><a className="hover:underline hover:text-blue-500 hover:bg-yellow-300 transition-colors duration-300" href="https://www.linkedin.com/in/raghavtirumale/" target="_blank" rel="noopener noreferrer">Raghav Tirumale</a></li>
                        <li className="m-4"><a className="hover:underline hover:text-blue-500 hover:bg-yellow-300 transition-colors duration-300" href="https://www.linkedin.com/in/lex-ibanez" target="_blank" rel="noopener noreferrer">Lex Ibanez</a></li>
                        <li className="m-4"><a className="hover:underline hover:text-blue-500 hover:bg-yellow-300 transition-colors duration-300" href="https://www.linkedin.com/in/ram-n-reddy/" target="_blank" rel="noopener noreferrer">Ram Reddy</a></li>
                        <li className="m-4"><a className="hover:underline hover:text-blue-500 hover:bg-yellow-300 transition-colors duration-300" href="https://www.linkedin.com/in/tianhao-chen-89b8a7297/" target="_blank" rel="noopener noreferrer">Tianhao Chen</a></li>
                    </ul>
                </div>
            </div>
            </div>
        </div>
    );
}