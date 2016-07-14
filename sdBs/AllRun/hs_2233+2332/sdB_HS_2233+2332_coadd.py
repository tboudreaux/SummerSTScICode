from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[338.946167,23.794367],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_2233+2332/sdB_HS_2233+2332_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_2233+2332/sdB_HS_2233+2332_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()