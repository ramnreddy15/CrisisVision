
import Navbar from "../components/navbar";
import { Lexend } from "next/font/google";


const lexend = Lexend({ subsets: ["latin"] })

export default function Page() {
    return (
        <div classname='w-screen h-[1000px] bg-[#252422] ${lexend.className}'>
            <Navbar></Navbar>
            <div className="w-full h-[900px] bg-[#252422]">
                <div className='relative text-6xl text-[#EB5E28] top-[150px] left-[7.5%] w-[85%] flex justify-center'>
                    Purpose
                </div>
               
            </div>
            <div>
            <div className="absolute bg-[#403D39] rounded-md h-[250px] w-[90%] left-[7.5%] top-[250px] text-xl text-white flex flex-wrap text-pretty justify-center items-center">
                <div className="p-10">
                    <p className="text-center">From 2018 to 2022, they have caused over $600 billion in damages and 1,751 deaths. In 2022, 96 Firefighters were killed while on duty.
                    Search and rescue is crucial during situations such as natural disasters to save lives. An important part of an effective search and rescue 
                    operation is the ability quickly and effectively assess a situation and decide how to proceed. However, these natural disasters  can present 
                    dangers to the search and rescue teams, as the harsh weather conditions and unstable terrain can pose a risk to their safety. We aimed to create 
                    a device that can autonomously collect data that the search and rescue team can use the assess the situation without risking their safety.</p>
                    </div>
                </div>
                <div className="absolute bg-[#403D39] rounded-md h-[250px] w-[90%] left-[7.5%] top-[550px] p-10 text-xl text-white flex flex-wrap text-pretty justify-center items-center">
                <p className="text-center">People often can get stranded and trapped as a result of the rubble and destruction caused by
                  them. Because of this, Search and Rescue is crucial to save lives. However, these dangerous conditions can endanger the SAR responders.
                 Being able to quickly assess the situation is important for these operations, but ensuring responder's safety is equally as important. That's why we created an 
                 autonomous vehicle that can help SAR teams survey an area. CrisisVision can autonomously navigate dangerous environments and give a live feed of what it sees. 
                 It can also recognize objects, hazards, or people in distress.</p>
                </div>
            </div>
        </div>
    );
}