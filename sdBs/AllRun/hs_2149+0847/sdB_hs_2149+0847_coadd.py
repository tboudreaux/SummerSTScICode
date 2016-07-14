from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[327.97625,9.022594],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_2149+0847/sdB_hs_2149+0847_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_2149+0847/sdB_hs_2149+0847_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
