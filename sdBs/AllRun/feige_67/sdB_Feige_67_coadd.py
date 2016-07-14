from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[190.46575,17.522606],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Feige_67/sdB_Feige_67_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Feige_67/sdB_Feige_67_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
