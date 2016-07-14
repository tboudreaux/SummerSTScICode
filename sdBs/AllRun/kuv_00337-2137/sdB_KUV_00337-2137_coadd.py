from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[9.039083,-21.348481],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_00337-2137/sdB_KUV_00337-2137_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_00337-2137/sdB_KUV_00337-2137_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
