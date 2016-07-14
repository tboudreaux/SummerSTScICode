from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[34.468042,9.100364],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_0215+0852/sdB_hs_0215+0852_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_0215+0852/sdB_hs_0215+0852_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
