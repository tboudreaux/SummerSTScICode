from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[73.599667,75.845756],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_0447+7545/sdB_hs_0447+7545_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_0447+7545/sdB_hs_0447+7545_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
