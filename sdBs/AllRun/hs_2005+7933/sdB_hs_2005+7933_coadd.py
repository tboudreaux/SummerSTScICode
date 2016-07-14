from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[300.66975,79.698125],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_2005+7933/sdB_hs_2005+7933_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_2005+7933/sdB_hs_2005+7933_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
