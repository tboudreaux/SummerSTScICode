from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[33.981292,23.720667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_0213+2329/sdB_hs_0213+2329_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_0213+2329/sdB_hs_0213+2329_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
