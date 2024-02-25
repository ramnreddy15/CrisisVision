'use client'
import { useState } from "react";
import Navbar from "../components/navbar";

export default function Page() {
    return (
        <div classname='w-screen h-[3000px] bg-[#252422]'>
            <Navbar></Navbar>
            <div className="text-black h-[3000px] bg-[#252422]">
                <div className='relative text-6xl text-white top-[150px] left-[7.5%] w-[85%] flex justify-center'>
                    The purpose
                </div>
                <div className="relative h-full w-[85%] bg-red-100 left-[7.5%] top-[200px]">

                </div>
            </div>
        </div>
    );
}