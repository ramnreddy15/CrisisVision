'use client'
import { useState } from "react";
import Navbar from "../components/navbar";

export default function Page() {
  return (
    <div classname='w-screen bg-[#252422]'>
      <Navbar></Navbar>
      <div className="text-black h-[2000px] bg-[#252422]">
        <div className='relative text-6xl text-[#EB5E28] top-[150px] left-[7.5%] w-[85%] flex justify-center'>
          Videos
        </div>
        <div className="relative h-full w-[85%] left-[7.5%] top-[200px] flex flex-col justfiy-center gap-[110px]">
          <div className="w-full h-auto flex flex-wrap justify-space-between justify-center items-center gap-[110px] ">
          <iframe width="560" height="315" src="https://www.youtube.com/embed/QEDnYhGgfKs?si=TwfC4a-m_svb5Us1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
          <iframe width="560" height="315" src="https://www.youtube.com/embed/kV3XZdZel-U?si=zQSNzdy6V-rE0Uhv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
          </div>
          <div className="w-full h-auto flex flex-wrap justify-space-between justify-center items-center gap-[110px] ">
            
          </div>
        </div>
        
      </div>
    </div>
  );
}