from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[25.78125,-38.554519],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SB_705/sdB_SB_705_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SB_705/sdB_SB_705_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
