from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[335.316875,32.087692],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_2218+3150/sdB_HS_2218+3150_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_2218+3150/sdB_HS_2218+3150_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
