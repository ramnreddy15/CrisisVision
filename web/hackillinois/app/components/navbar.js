'use client'
import Image from "next/image";
import { useState } from "react";
import Link from "next/link";

export default function Navbar() {
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

    return (
        <div className="text-white w-full h-17 z-10 pt-1 fixed items-center" style={{backgroundColor: asdf}}>
            <div className="w-full h-full flex flex-row justify-between items-center p-7 pl-9 pr-9">
                <div className="flex flex-row gap-12 font-ander font-bold text-2xl">
                    <Link href='/' className="hover:underline">
                        crisisvision.
                    </Link>
                </div>
                <div className="gap-10 flex flex-row">
                    <Link href='/purpose' className="hover:underline">
                        Purpose
                    </Link>
                    <Link href='/team' className="hover:underline">
                        Team
                    </Link>
                    <Link href='/videos' className="hover:underline">
                        Videos
                    </Link>
                    <Link href='/about' className="hover:underline">
                        About
                    </Link>
                </div>
            </div>

        </div>

    );
}