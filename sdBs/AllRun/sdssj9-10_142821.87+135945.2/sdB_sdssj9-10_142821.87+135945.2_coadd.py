from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[217.091125,13.995889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_142821.87+135945.2/sdB_sdssj9-10_142821.87+135945.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_142821.87+135945.2/sdB_sdssj9-10_142821.87+135945.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
