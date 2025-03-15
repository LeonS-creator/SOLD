"use client";  // ✅ This tells Next.js to treat it as a client-side component

import { useState } from "react";
import { QRCodeCanvas } from "qrcode.react"; // ✅ Correct import

export default function Home() {
  const [userType, setUserType] = useState<"customer" | "business">("customer");
  const [name, setName] = useState<string>("");
  const [qrCode, setQrCode] = useState<string | null>(null);

  const registerUser = async () => {
    const endpoint =
      userType === "business"
        ? "http://localhost:8000/register/business/"
        : "http://localhost:8000/register/user/";


    // const endpoint =
    //   userType === "business"
    //     ? "http://127.0.0.1:8000/register/business/"
    //     : "http://127.0.0.1:8000/register/user/";

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name }),
      });
      const data = await response.json();
      setQrCode(data.qr_code);
    } catch (error) {
      console.error("Error registering user:", error);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen space-y-4">
      <h2 className="text-xl font-semibold">Register as {userType}</h2>

      <div className="flex space-x-4 mb-4">
        <button
          onClick={() => setUserType("customer")}
          className={`p-2 border ${userType === "customer" ? "bg-blue-500 text-white" : ""}`}
        >
          Customer
        </button>
        <button
          onClick={() => setUserType("business")}
          className={`p-2 border ${userType === "business" ? "bg-green-500 text-white" : ""}`}
        >
          Business
        </button>
      </div>

      <input
        type="text"
        placeholder="Enter Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        className="p-2 border"
      />
      <button onClick={registerUser} className="p-2 bg-blue-600 text-white">
        Register
      </button>

      {qrCode && (
        <div className="mt-4">
          <h2 className="text-lg font-semibold">Your QR Code</h2>
          <QRCodeCanvas value={qrCode} size={200} />
        </div>
      )}
    </div>
  );
}
