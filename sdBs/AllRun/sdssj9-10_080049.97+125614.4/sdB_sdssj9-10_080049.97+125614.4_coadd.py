from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[120.208208,12.937333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_080049.97+125614.4/sdB_sdssj9-10_080049.97+125614.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_080049.97+125614.4/sdB_sdssj9-10_080049.97+125614.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
