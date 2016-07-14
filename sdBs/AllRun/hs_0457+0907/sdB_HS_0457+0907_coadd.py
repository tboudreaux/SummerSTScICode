from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[75.07875,9.201278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_0457+0907/sdB_HS_0457+0907_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_0457+0907/sdB_HS_0457+0907_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
