
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
                    <p className="text-center">
                        In the span from 2018 to 2022, natural disasters have inflicted over $600 billion in damages and claimed the lives of 1,751 individuals.
                        Tragically, in 2022 alone, 96 firefighters lost their lives while bravely serving on duty. These statistics underscore the critical importance of 
                        search and rescue (SAR) operations during such calamities, where every second can mean the difference between life and death.

                        The ability to swiftly and accurately assess a crisis situation is pivotal for effective SAR operations. However, the very nature of 
                        natural disasters exposes SAR teams to perilous conditions, including harsh weather and unstable terrain, heightening the risk to their safety.</p>
                    </div>
                </div>
                <div className="absolute bg-[#403D39] rounded-md h-[325px] w-[90%] left-[7.5%] top-[550px] p-10 text-xl text-white flex flex-wrap text-pretty justify-center items-center">
                <p className="text-center">In response to these challenges, we have developed an innovative solution: CrisisVision, an autonomous vehicle designed to gather essential data without
                 jeopardizing the safety of SAR teams. In disaster zones where individuals may become stranded or trapped amid rubble and destruction, SAR intervention becomes indispensable.

                CrisisVision serves as an indispensable ally to SAR teams, autonomously navigating treacherous environments while providing real-time visual feedback. Its advanced technology 
                enables it to identify objects, hazards, and individuals in distress, empowering SAR personnel with critical information for informed decision-making.

                By deploying CrisisVision, SAR operations become more efficient and effective, minimizing the need for direct human exposure to danger. Our mission is clear: to safeguard the 
                lives of both those in distress and the courageous responders who selflessly serve on the frontlines of disaster relief.</p>
                </div>
            </div>
        </div>
    );
}