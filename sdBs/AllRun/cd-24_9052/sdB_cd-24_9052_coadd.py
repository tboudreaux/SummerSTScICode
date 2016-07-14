from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[156.462083,-24.889003],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_cd-24_9052/sdB_cd-24_9052_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_cd-24_9052/sdB_cd-24_9052_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
