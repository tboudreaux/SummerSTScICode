from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[120.562,-3.971167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bd-3_2179/sdB_bd-3_2179_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bd-3_2179/sdB_bd-3_2179_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
