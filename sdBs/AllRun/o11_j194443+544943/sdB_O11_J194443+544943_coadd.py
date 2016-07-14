from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[296.179167,54.828611],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_O11_J194443+544943/sdB_O11_J194443+544943_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_O11_J194443+544943/sdB_O11_J194443+544943_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
