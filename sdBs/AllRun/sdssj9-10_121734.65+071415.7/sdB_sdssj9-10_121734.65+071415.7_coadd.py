from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[184.394375,7.237694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_121734.65+071415.7/sdB_sdssj9-10_121734.65+071415.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_121734.65+071415.7/sdB_sdssj9-10_121734.65+071415.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
