from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[252.477292,48.448181],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Bal_83600004/sdB_Bal_83600004_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Bal_83600004/sdB_Bal_83600004_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
