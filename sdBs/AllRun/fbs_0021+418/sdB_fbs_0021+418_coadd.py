from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[5.980083,42.151361],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0021+418/sdB_fbs_0021+418_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0021+418/sdB_fbs_0021+418_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
